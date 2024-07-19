'use client'
import CarouselBanner from '../components/CarouselBanner/CarouselBanner';
import Menu from '../components/Menu';
import Card from '../components/Card';
import Taba from '@/components/Taba/Taba';
import SubMenu from '@/components/SubMenu/Index';

export default function Home() {
  return (
    <>
      <Menu className="flex justify-end max-w-xl" />
      <SubMenu />
      <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <CarouselBanner />

        <Card description={'aloha caption'} title={'title aqui'} />
      </main>
    </>
  );
}